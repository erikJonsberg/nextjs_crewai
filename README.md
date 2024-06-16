# Crewai Company Research Assistant

## Overview

This project uses a crew of AI assistants to search for blog posts and YouTube videos based on company and position. For example: Giving the AI `Tesla` and `CEO` would yield a list of articles and videos about Elon Musk.

This project is my first deep dive into CrewAI.

It features Next.js (React Javascript) on the front-end and CrewAI (Python) on the back-end.

CrewAI is a:

> Cutting-edge framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

It basically allows for the setup of two or more AI assistants to work together to carry out tasks. One of the AIs is a manager that delegates tasks to the agents. The manager is responsible for assembling the main task from the subtasks carried out by the agents. By working together in this manner, the crew is more efficient than a single AI assistant.

## Installation

The local environment needs to be running `Python` version 3.10 or higher.

### Install the back-end

From the `root` directory

```bash
cd crewai_be
```

Install project dependencies

```bash
poetry install --no-root
```

Run the Poetry shell

```bash
poetry shell
```

Run the server

```bash
python api.py
```

### Install the front-end

From the `root` directory

```bash
cd nextjs_app
```

Install dependencies

```bash
npm install
```

Run the development server

```bash
npm run dev
```

To learn more about Next.js and CrewAI, take a look at the following resources:

-   [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
-   [CrewAI Documentation](https://docs.crewai.com/) - learn about CrewAI features and API.

You can check out [the Next.js](https://github.com/vercel/next.js/), and [CrewAI](https://github.com/joaomdmoura/crewai) GitHub repositories.
