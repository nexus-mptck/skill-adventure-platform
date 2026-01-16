const express = require('express');
const axios = require('axios'); // To call the Python API
const app = express();
app.use(express.json());

// Endpoint to receive results from the browser game
app.post('/api/submit-game', async (req, res) => {
    const studentData = req.body;

    try {
        // Forward data to the Python AI service
        const aiResponse = await axios.post('http://127.0.0.1:8000/analyze', studentData);
        
        // Return the AI analysis back to the student's dashboard
        res.json({
            message: "Assessment Complete!",
            results: aiResponse.data
        });
    } catch (error) {
        res.status(500).json({ error: "AI Service is offline" });
    }
});

app.listen(3000, () => console.log('Web Server running on http://localhost:3000'));
