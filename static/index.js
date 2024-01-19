$(document).ready(() => {

    // Weather click handler
    $('#weather').click(function () {
        $.ajax({
            url: '/weather',
            type: 'GET',
            success: function (data) {
                // Update DOM elements with weather data
                $('#temperature').text("Currently : " + data[0]["Temperature"] + "°F");
                $('#name').text(data[0]["Name"]);
                $('#forecast').text(data[0]["Detailed Forecast"]);
                $('#name2').text(data[1]["Name"]);
                $('#temperature2').text(data[1]["Temperature"]);
                $('#forecast2').text(data[1]["Detailed Forecast"]);
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    });

    // Storage click handler
    $('#storage').click(function () {
        $.ajax({
            url: '/storage',
            type: 'GET',
            success: function (data) {
                // Update DOM element with storage data
                $('#storage').text(data);
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    });

    // Bandwidth click handler
    $('#bandwidthbtn').click(function () {
        $.ajax({
            url: '/bandwidth',
            type: 'GET',
            success: function (data) {
                // Update DOM element with converted data
                $('#bandwidth').text(JSON.stringify(data.eth0));
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    });
    
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

    // Fetch uptime every second
    setInterval(fetchUptime, 1000);

    // Fetch utilization every 5 seconds
    setInterval(fetchUtilization, 5000);
});
