function human(id) {
    click = 'moon' + id
    document.getElementById(click).src = 'https://i.ya-webdesign.com/images/moon-art-png.png'
    $(function() {
        $.ajax({
            type: 'POST',
            url: "/jstoflask",
            data: {
                position: id
            },

            success: function(data) {
                console.log('success', data);
                document.get
            }
        });
    });
}
document.getElementsByTagName