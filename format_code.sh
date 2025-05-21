#!/bin/bash

echo "📦 Installing autopep8..."
pip install autopep8

echo "🧼 Formatting all .py files in 'app/'..."
autopep8 --in-place --aggressive --aggressive --recursive app/

echo "✅ Done! All Python files in 'app/' formatted."
