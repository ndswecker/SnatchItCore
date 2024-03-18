
# SnatchIt

Welcome to SnatchIt, a Django-based web application developed in Python for the real-time submission and management of bird banding records. SnatchIt embraces server-side rendering for generating HTML content dynamically, enhancing the user experience with fast and responsive web pages.

## Features

SnatchIt is packed with features designed to support ornithologists and bird banding professionals:

- **Server-Side Rendering**: Utilizes Python and Django for dynamic HTML generation, ensuring fast page loads and a seamless user experience.
- **Bootstrap 5**: Employs Bootstrap 5 for modern, responsive HTML element styling and functionality, offering an optimal viewing experience across all devices.
- **Crispy Forms**: Leverages Crispy Forms for rendering Django forms, making form creation and management straightforward and efficient.
- **Authentication**: Incorporates Django's built-in authentication system with JWT support for secure user registration and login processes.
- **User and Admin Management**: Utilizes Django's built-in functionalities for managing user and admin accounts, streamlining the administration process.
- **MAPS Banding Protocol Support**: Currently supports the Monitoring Avian Productivity and Survivorship (MAPS) banding protocol, with a modular design that allows for future expansion to include additional protocols.
- **Comprehensive Validation**: Implements over 20 validations to ensure the accuracy and integrity of submitted data.
- **Mobile-Friendly Design**: Optimized for mobile devices, facilitating field submissions directly from a mobile phone or tablet.
- **Miniature Pyle Guide**: Integrates a miniaturized version of the Identification Guide to North American Birds (2nd edition) by Pyle for quick reference.
- **Extensive Species Support**: Supports over 75 bird species that breed in the Pacific Northwest, tailored for use by the Puget Sound Bird Observatory (PSBO) for MAPS.
- **Data Export**: Enables the export of records to the USGS CSV upload template or the Institute for Bird Populations (IBP) template for broader data sharing and analysis.

## Installation

To install SnatchIt, ensure you have Python version 3.10 or higher installed on your machine. Then, execute the appropriate installation script for your operating system:

**Powershell:**

```shell
.\scripts\install


## Getting Started

### Prerequisites

1. Python >= 3.10

### Installation

Execute the appropriate `install` script for your machine:

Powershell:

```shell
.\scripts\install
```

Command Prompt:

```shell
scripts\install
```

Bash:

```shell
./scripts/install.sh
```

### Building & running the Application

Execute the appropriate `run` script for your machine:

Powershell:

```shell
.\scripts\run
```

Command Prompt:

```shell
scripts\run
```

Bash:

```shell
./scripts/run.sh
```

## Deploy

See the deployment [README.md](./deploy/README.md)

## Code Quality

This project uses pre-commit to enforce style and standards

```shell
pre-commit run --all-files
```

## Testing
To Test the maps functionalities:

```py app/manage.py test maps ```
