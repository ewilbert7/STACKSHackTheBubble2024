# Candidate Connect

Section 419 Presents

## Project Overview

**Candidate Connect** is an interactive voter assistance tool designed to remove bias, educate voters, and boost democratic engagement. By presenting users with policy statements and capturing their reactions using facial emotion recognition, Candidate Connect identifies the candidate whose policies align most closely with each user’s values. This approach allows voters to make more informed choices based on policies rather than intuition or personal biases.

## Goals

- **Remove Bias**: Helps voters focus on policy alignment instead of personal bias.
- **Educate Voters**: Provides insights into candidate policies on key issues.
- **Boost Interactivity**: Engages users through real-time interaction and feedback.
- **Improve Democracy**: Encourages fact-based voting and informed decisions.

## Why Candidate Connect?

According to the BBC, many people vote based on intuition and personal preferences rather than informed consideration of policies. Candidate Connect addresses this by matching voters with candidates who align with their values. The app presents a series of policy statements and gauges the user's reactions to identify the best match, making it easier for voters to focus on relevant issues.

## How It Works

- **User Interface**: Built with Pygame to create a simple, engaging UI.
- **Emotion Recognition**: Uses OpenCV and facial emotion recognition to capture user reactions to policy statements.
- **Data Sourcing**: Policies are gathered from reliable sources, covering topics like the economy, worker rights, immigration, and more.
- **Candidate Scoring**: Based on user responses, a score is calculated for each candidate to determine the best fit.

## Tech Stack

- **Frontend**: Pygame (Python)
- **Emotion Detection**: OpenCV, FER (Facial Emotion Recognition library)
- **Data Format**: JSON for storing candidate policies

## Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ewilbert7/STACSHackTheBubble2024.git
    cd STACSHackTheBubble2024
    ```

2. **Set up a virtual environment** (optional):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```

5. **Access the app**:
   The application runs in a local Pygame window.

## Usage

1. Launch the app and start the questionnaire.
2. React to each policy statement on screen. The app uses facial emotion detection to capture these reactions.
3. At the end, the app displays your best candidate match based on your reactions.

## Demo

**Demo conducted by Michael**: For a complete walkthrough, refer to our demonstration video (if available) or the demo section in this repository.

## Future Enhancements

- **Enhanced Emotion Detection**: Improve accuracy with a larger dataset and advanced facial recognition models.
- **Additional Candidate Profiles**: Expand the app with more candidates and policies for broader applicability.
- **Mobile Support**: Extend support to mobile devices for easier accessibility.

## Contributors

- [Eworitsewarami Wilbert](https://github.com/ewilbert7)
- [Osi Mayungbo](https://github.com/01m1)
- [Nifemi Awotorebo](https://github.com/nifemiawo)
- [Michael Abayomi-Ojumu](https://github.com/Michael-A05)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
