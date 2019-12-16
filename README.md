# Evaluately

[![ForTheBadge powered-by-electricity](http://ForTheBadge.com/images/badges/powered-by-electricity.svg)](http://ForTheBadge.com)
[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Actions Status](https://github.com/mmookptr/evaluately/workflows/Evaluately/badge.svg)](https://github.com/mmookptr/evaluately/actions)
[![GitHub issues](https://img.shields.io/github/issues/mmookptr/evaluately.svg)](https://GitHub.com/mmookptr/evaluately/issues/)
[![Tweeting](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Evaluately%20is%20awesome!)
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://evaluately.herokuapp.com/)

> This repository is part of ISP2019 course

# Project description

Evaluately provides a customizable web-based evaluation form with data summarization and status reporting. Event organizers can create a custom form for their event containing a list of entrants (contestants, projects, presentors, performers, etc) and a set of criteria that they are to be rated on. Criteria may also include guidance (help) on ratings. There may optionally be space for entering comments.
The event organizers control who can view and submit an evaluation, and the time interval during which submission is allowed. The organizers can elect to allow self-registration for open events.
The application authenticates each person who submits a form and ensures only one evaluation per person, although a person may revise and resubmit a prior submission, and evaluations may be submitted incrementally. The application provides a status display for organizers that shows who has submitted an evaluation and whether its complete or not, but does not allow the organizer to view content of the evaluation.
After the submittal period has ended, the application displays a summary of evaluations or scores, and provides access to comments. It may limit who can view comments.
At some events the entrants/contestants are also allowed to submit evaluations. Students at KU can submit a senior project evaluation or vote at Exceed Camp even if they have a project entered in the competition. The organizer can specify whether this is allowed and whether or not someone may evaluate his own project.

# Requirements

The application requires

**Python** (v.3.6 or newer)

**Django** (v 2.2 or newer)

**Python Add-On Modules** on [requirements.txt](requirements.txt)

# Installation

## 1.Clone this repository

via SSH

     git clone git@github.com:mmookptr/evaluately.git

via HTTPS

     git clone https://github.com/mmookptr/evaluately.git

## 2. Access it

     cd evaluately

## 3.Install requirements

     pip3 install -r requirements.txt

## 4.Migrate

     python3 manage.py migrate

## 5.Run Server

     python3 manage.py runserver

## 6.Redirect to the site from your favorite browser

> http://localhost:8000/

# Member

- Sidtipat Kietchai (Facilicator, Coder)
- Patteera Likitamnuayporn (Designer, Coder)
- Nattaphon Rakprokobkij (Director ,Coder)
- Pakkapon Visuttitewin (Qa manager, Coder)

## CI/CD with GitHub Actions

https://github.com/mmookptr/evaluately/actions

GitHub Actions provide huge versatility and the integration is almost seamless. Please check GitHub actions for yourself, create a workflow of your own and see whether/how it improves your current development life cycle.

## Trello Board URL

[Trello Board](https://trello.com/b/bICn1NIa/evaluately)

## Project Backlog URL

[Iteration Plans](https://docs.google.com/document/d/1tbbW8fQMx2SEDQTjB0Jtj4mknjqA_rKx_tdUeCVFEqs/edit#heading=h.e1kzr3qblvqo)

## Iteration Retrospective

[Retrospective](https://docs.google.com/document/d/1__I9L3fENzzlq_ilo4gY-A2EZMFPoNFcl1jnn4KBaYM/edit?usp=sharing)
