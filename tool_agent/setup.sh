#!/bin/bash

# Streamlit Cloud Setup Script
# Usage: ./setup.sh <agent_folder>

AGENT=$1

if [ -z "$AGENT" ]; then
    echo "Usage: ./setup.sh <agent_folder>"
    echo "Example: ./setup.sh tool_agent"
    exit 1
fi

echo "Setting up $AGENT for Streamlit Cloud..."

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py --server.headless true
