#!/usr/bin/env python3
"""Regenerate GC UI PNG derivatives from canonical SVG (PyGObject Rsvg + pycairo)."""
from pathlib import Path
import argparse
import struct
import gi
import cairo

gi.require_version("Rsvg", "2.0")
from gi.repository import Rsvg

ROOT = Path(__file__).resolve().parents[1]
SIZES = {
    "app-icon": [16, 32, 48, 64, 72, 96, 128, 144, 180, 192, 256, 512, 1024],
    "app-icon-monochrome": [192, 512],
    "gc-ui-symbol": [64, 128, 256, 512],
    "gc-ui-logo": [553, 1106],
    "gc-ui-logo-dark": [553, 1106],
}

def make(name, width):
    svg = ROOT / (name + ".svg")
    handle = Rsvg.Handle.new_from_file(str(svg))
    dimensions = handle.get_dimensions()
    height = round(width * dimensions.height / dimensions.width)
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    context = cairo.Context(surface)
    context.scale(width / dimensions.width, height / dimensions.height)
    if not handle.render_cairo(context):
        raise RuntimeError(f"SVG rendering failed: {svg.name}")
    output = ROOT / f"{name}-{width}.png"
    surface.write_to_png(str(output))
    return output, height

def verify(path, width, height):
    with path.open("rb") as f:
        data = f.read(24)
    if data[:8] != b"\x89PNG\r\n\x1a\n" or struct.unpack(">II", data[16:24]) != (width, height):
        raise ValueError(f"Invalid PNG: {path.name}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    count = 0
    for name, widths in SIZES.items():
        for width in widths:
            if args.verify:
                path = ROOT / f"{name}-{width}.png"
                height = round(width * (190 / 553)) if name.startswith("gc-ui-logo") else width
            else:
                path, height = make(name, width)
            verify(path, width, height)
            count += 1
    print(f"GC UI: {count} canonical SVG-derived PNGs {'verified' if args.verify else 'generated'}.")

if __name__ == "__main__":
    main()
