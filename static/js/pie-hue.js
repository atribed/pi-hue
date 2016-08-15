// Config settings

(function() {
    var apiUsername = 'exampleusername'; // This is super gross. Will move it to server and proxy once things are working.
    var bridgeAddress = 'http://0.0.0.0'; // path to bridge (should be IP)

    // Dirty take picture request, will clean.
    function requestPicture() {
        $.ajax({
            url: '/picture',
            method: 'POST',
            data: {
                picture: true
            }
        });
    }

    // Gets group info from server.
    function getGroupInfo() {
        var groupRequest = $.ajax({
            url: bridgeAddress + '/api/' + apiUsername + '/groups/'
        });

        return groupRequest;
    }

    // Sends a request to get groups and finds the ID for the one you want.
    function getGroupIdByName(groupName, callback) {
        var groupInfoRequest = getGroupInfo();

        groupInfoRequest.done(function(data) {
            var groupId = '';
            _.each(data, function(group, id) {
                if (group.name === groupName) {
                    groupId = id;

                    return;
                }
            });

            callback(groupId);
        });
    }

    // Sets group settings by a group name.
    function setGroupSettingsByName(name, setting, value) {
        var data = {};
        data[setting] = value;

        var callback = function(id) {
            $.ajax({
                url: bridgeAddress + '/api/' + apiUsername + '/groups/' + id + '/action',
                data: window.JSON.stringify(data),
                type: 'PUT'
            });
        };

        getGroupIdByName(name, callback);
    }

    // Quick and dirty, will refactor after sleep.
    function setColorTemp(event) {
        event.preventDefault();
        $target = $(event.target);

        var value = $target.find('[name="ct"]').val();
        var room = $target.find('[name="room"]').val();

        setGroupSettingsByName(room, 'ct', parseInt(value, 10));
    };

    $(document).ready(function() {
        window.console.log('Pi-Hue has loaded JS successfully!');

        // Takes a picture with the pi.
        $('#takePicture').click(requestPicture);

        // Changes color temp.
        $('#setCt').submit(setColorTemp);
    });
})();
