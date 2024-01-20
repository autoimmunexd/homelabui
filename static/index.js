$(document).ready(() => {

    const fetchBandwidth = () => {
        $.ajax({
            url: '/bandwidth',
            type: 'GET',
            success: (data) => {
                // Update DOM element with converted data
                $('#bandwidth').text(JSON.stringify(data.eth0));
            },
            error: (error) => {
                console.error('Error:', error);
            }
        });
    };

    // Function to fetch uptime and update DOM every second
    const fetchUptime = () => {
        $.get(`/uptime?${new Date().getTime()}`, (data) => {
            $('#uptime').text(`Uptime: ${data}`);
        });
    };

    // Function to fetch utilization and update DOM every 5 seconds
    const fetchUtilization = () => {
        $.get(`/utilization?${new Date().getTime()}`, (data) => {
            // Update DOM elements with utilization data
            $('#cpu').text(`CPU: ${data.cpu}`);
            $('#memory').text(`Memory: ${data.mem}`);
        });
    };

    const fetchData = () => {
        fetch('/storage', {
            method: 'GET',
        })
        .then(response => response.text())
        .then(data => {
            // Update DOM element with storage data
            document.getElementById('storage').textContent = data;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    };

    const updateWeatherData = () => {
        $.ajax({
            url: 'static/data/ui_data.json', // Update the URL to point to the JSON file
            type: 'GET',
            dataType: 'json', // Specify the expected data type
            success: (data) => {
                // Update DOM elements with weather data
                $('#temperature').text(`Currently : ${data[0]["Temperature"]}°F`);
                $('#name').text(data[0]["Name"]);
                $('#forecast').text(data[0]["Detailed Forecast"]);
                $('#name2').text(data[1]["Name"]);
                $('#temperature2').text(data[1]["Temperature"]);
                $('#forecast2').text(data[1]["Detailed Forecast"]);
                $('#last-updated-weather').text(data[2]["Updated Last"])
            },
            error: (error) => {
                console.error('Error:', error);
            }
        });
    };

    //on page load
    fetchData();
    updateWeatherData();

    //interval timers for live data
    setInterval(fetchBandwidth, 5000)
    // Fetch uptime every second
    setInterval(fetchUptime, 5000);
    // Fetch utilization every 5 seconds
    setInterval(fetchUtilization, 5000);
    // Fetch storage every 30 minutes
    setInterval(fetchData, 30 * 60 * 1000);
});