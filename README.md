# 🌍 Trippy - Your AI Travel Planner

An intelligent travel planning web application that helps you plan budget-friendly trips with personalized recommendations for flights, hotels, and itineraries using AI.

## 🌐 Live Demo

**Access the live application:** [https://trippy-travel-planner.herokuapp.com](https://trippy-travel-planner.herokuapp.com)

## ✨ Features

- **Smart Flight Search**: Real-time flight data with instant booking links to Google Flights
- **Hotel Recommendations**: Personalized hotel suggestions based on your budget and preferences
- **AI-Powered Itineraries**: Custom day-by-day plans based on your interests and travel style
- **Interactive Chat Assistant**: Voice-enabled travel assistant for questions and trip planning
- **Budget Optimization**: Intelligent budget allocation across flights, hotels, and activities
- **User Accounts**: Save and manage your travel plans
- **Responsive Design**: Modern, beautiful UI that works on all devices
- **Real-Time Planning**: Live search results and instant recommendations

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Gemini AI API key ([Get here](https://makersuite.google.com/app/apikey))
- SERP API key ([Get here](https://serpapi.com/dashboard))

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Travel-Planner-AI-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example file
   copy .env.example .env
   
   # Edit .env file and add your API keys:
   # GEMINI_API_KEY=your_actual_gemini_api_key
   # SERP_API_KEY=your_actual_serp_api_key
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 🔧 Configuration

### API Keys Setup

#### Gemini AI API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key to your `.env` file

#### SERP API Key
1. Sign up at [SerpApi](https://serpapi.com/dashboard)
2. Get your free API key (100 searches/month)
3. Copy the key to your `.env` file

### Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
SERP_API_KEY=your_serp_api_key_here
FLASK_SECRET_KEY=your_random_secret_key_here
```

## 🎯 How to Use

### 1. Plan Your Trip
- Enter your origin and destination cities
- Select your travel dates
- Choose number of people
- Set your budget
- Select your interests (adventure, culture, food, etc.)
- Click "Plan My Trip"

### 2. Browse Results
- **Flights Tab**: View recommended flights within your budget
- **Hotels Tab**: See hotel options with ratings and amenities
- **Itinerary Tab**: Get a personalized day-by-day plan
- **Budget Tab**: See how your budget is allocated

### 3. Chat with AI Assistant
- Ask questions about destinations
- Get travel tips and recommendations
- Clarify details about your itinerary
- Get help with travel planning

## 🏗️ Project Structure

```
Travel-Planner-AI-agent/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Web interface
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
├── README.md           # This file
└── .gitignore         # Git ignore rules
```

## 🔍 API Endpoints

- `GET /` - Main web interface
- `POST /search` - Search for flights, hotels, and generate itinerary
- `POST /chat` - Chat with AI assistant
- `GET /suggestions` - Get destination suggestions based on interests

## 🎨 Features in Detail

### Smart Budget Allocation
- 40% for flights
- 35% for hotels  
- 25% for activities and food

### Interest-Based Planning
Choose from various interests:
- Adventure & Outdoor Activities
- Culture & Museums
- Food & Culinary Experiences
- Nature & Wildlife
- History & Architecture
- Nightlife & Entertainment
- Shopping & Markets
- Relaxation & Wellness
- Photography & Sightseeing
- Sports & Recreation

### AI-Powered Itinerary
The AI creates detailed daily plans including:
- Recommended attractions and activities
- Restaurant suggestions for all meals
- Transportation tips
- Budget breakdown for activities
- Local cultural insights
- Emergency contacts and important info

## 🛠️ Customization

### Adding New Interests
Edit the interests array in `templates/index.html`:

```javascript
// Add new interest tags
<div class="interest-tag" data-interest="your-interest">Your Interest</div>
```

### Modifying Budget Allocation
Update the budget percentages in `app.py`:

```python
flight_budget = budget * 0.4  # 40% for flights
hotel_budget = budget * 0.35  # 35% for hotels
activity_budget = budget * 0.25  # 25% for activities
```

### Customizing AI Responses
Modify the system prompts in the `TravelAgent` class methods to change AI behavior.

## 🚨 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Ensure your API keys are correctly set in the `.env` file
   - Check that your Gemini AI API key is active
   - Verify your SERP API quota hasn't been exceeded

2. **No Search Results**
   - Try different city names or airport codes
   - Adjust your budget range
   - Check your internet connection

3. **Chat Not Working**
   - Verify your Gemini API key is working
   - Check the browser console for errors

### Debug Mode
Run the app in debug mode for detailed error messages:

```bash
export FLASK_DEBUG=1  # On Windows: set FLASK_DEBUG=1
python app.py
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Search existing issues on GitHub
3. Create a new issue with detailed information

## 🌟 Future Enhancements

- [ ] User authentication and trip saving
- [ ] Integration with booking platforms
- [ ] Weather information integration
- [ ] Currency conversion
- [ ] Offline itinerary access
- [ ] Social sharing features
- [ ] Multi-language support
- [ ] Mobile app version

---

**Happy Traveling! 🎉**