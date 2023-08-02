$(document).ready(function () {
	$.ajax({
		method: 'GET',
		url: 'https://fourtonfish.com/hellosalut/?lang=fr',
		success: function (data) {
			$('DIC#hello').text(data.hello);
		}
	});
]);
