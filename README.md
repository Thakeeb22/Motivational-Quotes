# Daily Motivational Quote Generator

A CrewAI-powered application that generates personalized morning messages combining motivational quotes, productivity tips, and formatted task lists to help you start your day with purpose and clarity.

## Features

- **Motivational Quote Generation**: AI-powered generation of short, inspiring quotes (1-2 sentences)
- **Productivity Tips**: Daily one-line productivity advice
- **Task Formatting**: Converts comma-separated task lists into clean, organized bullet points
- **Morning Message Creation**: Combines all elements into a friendly, cohesive morning message
- **Multi-Agent System**: Uses CrewAI with specialized agents for different aspects of message creation

## Project Structure

```
motivational-quotes/
├── src/
│   └── main.py          # Main application entry point
├── config/              # Configuration directory
├── agents.yaml          # Agent configurations
├── tasks.yaml          # Task definitions
├── pyproject.toml      # Project dependencies and metadata
└── README.md           # This file
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd motivational-quotes
   ```

2. **Install dependencies**:
   ```bash
   pip install crewai python-dotenv
   ```
   
   Or if using uv:
   ```bash
   uv sync
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root and add any required API keys or configuration variables.

## Usage

Run the application:

```bash
python src/main.py
```

When prompted, enter your tasks for the day as a comma-separated list:

```
Enter tasks (comma-separated): Review project proposal, Call client meeting, Update documentation, Plan weekend activities
```

The application will generate a complete morning message including:
- A motivational quote
- A productivity tip
- Your tasks formatted as a clean bullet list
- All combined into a friendly morning message

## How It Works

The application uses three specialized CrewAI agents:

### 1. Quote Generator Agent
- **Role**: Quote Generator
- **Goal**: Generate short motivational quotes and productivity tips
- **Output**: JSON format with quote and tip

### 2. Task Formatter Agent
- **Role**: Task Formatter
- **Goal**: Convert comma-separated tasks into clean bullet lists (max 6 items)
- **Output**: Markdown bullet list

### 3. Morning Message Coordinator
- **Role**: Morning Message Coordinator
- **Goal**: Combine quote, tip, and formatted tasks into a cohesive morning message
- **Output**: Complete friendly morning message

## Configuration

### Agent Configuration (`agents.yaml`)
Defines the roles, goals, and backstories for each agent in the crew.

### Task Configuration (`tasks.yaml`)
Specifies the task descriptions, expected outputs, and agent assignments.

### Project Configuration (`pyproject.toml`)
Contains project metadata, dependencies, and build configuration.

## Example Output

```
=== Morning Message (final) ===

Good morning! 🌅

"Success is not final, failure is not fatal: it is the courage to continue that counts. Every small step forward is progress worth celebrating."

💡 Productivity Tip: Start your day by tackling the most challenging task first when your energy is at its peak.

Here's what's on your agenda today:
• Review project proposal
• Call client meeting
• Update documentation
• Plan weekend activities

Have a productive and fulfilling day ahead! 🚀
```

## Requirements

- Python 3.8+
- CrewAI
- python-dotenv

## Author

Muhammad Thakeeb Muhammad

## License

This project is open source. Please check the license file for more details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue in the repository.
