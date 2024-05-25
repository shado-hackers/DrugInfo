# DrugInfo

## Overview
DrugInfo, is designed to provide users with comprehensive information about medicines. It utilizes a dataset containing details about various medicines, including their product name, salt composition, price, manufacturer, description, and side effects
## Features
- **Medicine Information**: Users can retrieve detailed information about medicines by simply typing the name of the medicine they're interested in.
- **Extensive Database**: The bot has access to a large dataset comprising information about 195,606 medicines.
- **Close Match**: In case of a typo or slight variation in the medicine name, the bot suggests a close match to help users find the correct medicine information.


## Dependencies
- [Pyrogram](https://github.com/pyrogram/pyrogram): Python framework for Telegram Bot API.
- Other dependencies specified in the `requirements.txt` file.

## Usage
- Start the bot by sending the `/start` command.
- Type the name of the medicine you want information about, and the bot will provide detailed information if available.

## File Structure
```bash
telegram-medicine-bot/
│
├── configs/
│   ├── telegram.py              # Configuration file for Telegram API credentials
│   └── dataset.py               # Configuration file for dataset location or settings
│
├── core/
│   ├── drugload.py              # Module for loading medicine data from CSV
│   ├── search_drug.py           # Module for searching medicine information
│   └── close_match.py           # Module for finding closest match for medicine name
│
├── data/
│   └── medicine_dataset.csv     # CSV file containing medicine data
│
├── app.py                       # Main bot application file
│
├── requirements.txt             # File listing dependencies required by the bot
│
└── README.md                    # README file containing project information and instructions

```

## License
- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

The information provided by this Telegram Medicine Information Bot is for informational purposes only and should not be considered medical advice. This bot is intended to provide general information about medicines based on a dataset, but it is not a substitute for professional medical advice, diagnosis, or treatment.

Users are advised to consult a qualified healthcare professional before making any decisions regarding their health or the use of any medication mentioned by the bot. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read on this bot.

The creators and developers of this bot do not endorse or promote any specific medication or treatment. Any reliance you place on information from this bot is strictly at your own risk. The creators and developers shall not be liable for any damages arising from the use of this bot or the information provided by it.

