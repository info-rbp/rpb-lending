<div align="center">
	<a href="https://frappe.io/lending">
		<img src=".github/lending-logo.png" height="80px" width="80px" alt="Frappe Lending Logo">
	</a>
	<h2>RPB Lending</h2>
	<p align="center">
		<p>Loan management application built on Frappe and ERPNext</p>
	</p>

[![CI](https://github.com/frappe/lending/actions/workflows/ci.yml/badge.svg?branch=develop)](https://github.com/frappe/lending/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/frappe/lending/branch/develop/graph/badge.svg?token=0TwvyUg3I5)](https://codecov.io/gh/frappe/lending)

</div>

<div align="center">
	<img src=".github/lending-hero.png"/>
</div>

## Overview

`info-rbp/rpb-lending` is a Frappe app for loan origination and loan servicing. The current application is still runtime-coupled to Frappe and ERPNext and should be treated as the live system of record for the existing platform.

Core capabilities visible in the repository include:

- loan products, pricing, and repayment schedules
- loan leads and applications
- disbursement, repayment, and interest accrual
- collateral/security management
- delinquency and classification processing
- accounting-linked operations through ERPNext

## Current Production-Hardening Focus

This repository is being improved on two tracks:

1. Hardening the current Frappe application so the existing system is safer and more stable.
2. Defining the foundation for a future independent platform rebuild.

The recent hardening work in this repository focuses on:

- stricter validation on whitelisted API methods
- permission checks before sensitive write operations
- more reliable loan-lead conversion into loan applications
- better regression coverage for origination edge cases
- CI maintenance to avoid deprecated GitHub Actions behavior

## Local Development

This app expects a working Frappe Bench environment with ERPNext installed.

At a high level:

1. Create a Frappe Bench environment compatible with the app's target Frappe/ERPNext versions.
2. Install ERPNext.
3. Install this app into the bench.
4. Create a site and install `lending`.
5. Run tests with `bench --site <site> run-tests --app lending`.

## CI

CI is defined in `.github/workflows/ci.yml` and runs the server-side test suite in parallel containers against MariaDB.

## Modernization Direction

The long-term target is a clean-room redevelopment rather than a direct framework migration. The planned target stack is:

- Appwrite for auth, core data services, realtime, and backend application capabilities
- Cloudflare Pages, Workers, R2, Queues, and Zero Trust for delivery and edge operations
- a standalone modern frontend instead of Frappe Desk as the primary product surface

That future architecture should be built alongside the current system, not mixed into the operational Frappe codepaths prematurely.