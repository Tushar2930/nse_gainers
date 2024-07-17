const express = require('express');
const axios = require('axios');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 5000;

app.use(cors());

const fetchNseData = async (url, headers) => {
    try {
        const response = await axios.get(url, { headers });
        return response.data;
    } catch (error) {
        console.error('Error fetching data from NSE:', error.response ? error.response.data : error.message);
        throw error;
    }
};

app.get('/api/gainers', async (req, res) => {
    const url = "https://www.nseindia.com/api/live-analysis-variations?index=gainers";
    const headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.nseindia.com/market-data/top-gainers-losers",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Host": "www.nseindia.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    };

    try {
        const data = await fetchNseData(url, headers);

        // Store data
        const filename = `fo_securities_${new Date().toISOString().split('T')[0]}.json`;
        const filepath = path.join(__dirname, filename);
        fs.writeFileSync(filepath, JSON.stringify(data, null, 4));

        console.log(`Data for ${new Date().toISOString().split('T')[0]} saved to ${filename}`);
        res.json(data);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch data' });
    }
});

app.listen(port, () => {
    console.log(`Proxy server running at http://localhost:${port}`);
});
