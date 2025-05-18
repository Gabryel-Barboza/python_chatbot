#!/usr/bin/env/ bash
set -e

uv sync

fastapi run src/main.py
