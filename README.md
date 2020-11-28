# Welcome to the GFDx Analysis Automation [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/nanthony007/gfdx/main/gfdx/app.py)

## Project Location
This project can be found [here](https://gfdx-automation.herokuapp.com)

## Project Actions
This project runs a series of analysis each night.

The analysis will run automatically every night at 1:30 AM EST.

If you wish to run the analysis manually you can click the “Run Analysis” button on the website.

***Be cautious this can take some time.*

A new analysis can be added by contacting Nick (see below).

The steps for adding new analysis are:
- Build the analysis in a jupyter notebook or similar environment
- Add documentation and explanations to your analysis
- Verify your analysis works as intended
- Send and communicate analysis to Nick and he will add to the automation by converting it to a python script 

## Project Contacts
- [Nick Anthony](nanthony007@gmail.com) (Technical Support)
- [Michelle Duong](michelledg0326@gmail.com) (Analysis Questions)


## General

Docs hosted by GitHub pages built using Mkdocs.
Streamlit app run using Heroku.
Coverge with Code Cov.
Testing with Pytest.

## Components

This project has three main components.

1. The web app
2. The data app
3. The notebooks

## The web app

This application is written in Python using Streamlit as a web base due to its simplicty. This app serves as a web-based entrypoint to automate and manually run analysis.

## The data app

This application is written in Python and aims to standardize and structure the GFDX data source.

## The notebooks

These notebooks are written in Python and serve as the foundation for the entire application. The notebooks contain the analysis code with comments and explanations. The code here is meant to be as simple as possible while achieving the desired outcomes and thus notebooks should contain Markdown and visualizations to improve communicability.
