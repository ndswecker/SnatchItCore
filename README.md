
# SnatchItCore

Welcome to SnatchItCore, a cutting-edge C# .NET Core 8 Web API designed specifically for bird banders adhering to the Micro Aging protocol. Our API facilitates the seamless submission of data and photos to a cloud-based database, streamlining the process of tracking and managing bird banding records.

## Features

SnatchItCore offers a comprehensive suite of features to support bird banders, including:

- **User Registration**: Allows new banders to register and join the community.
- **Authentication and Authorization**: Secure login process with JWTs (JSON Web Tokens) to ensure data security and integrity.
- **Bander Information Management**: Easy management and updating of bander profiles and credentials.
- **Data Record Uploads**: Facilitates the upload of bird banding data records to a centralized cloud database.
- **Record Viewing**: Enables users to view their submitted records in the database, enhancing data accessibility and usability.

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
