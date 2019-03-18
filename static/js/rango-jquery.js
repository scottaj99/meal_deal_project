$(document).ready( function() {

	$("p").hover( function() {
		$(this).css('color', 'red');
	},

	function() {
		$(this).css('color', 'blue');
	});

	$("#dialog").dialog({
		autoOpen: false,
		open: function(event, ui) { jQuery('.ui-dialog-titlebar-close').hide(); },
		show: {
			effect: "explode",
			duration: 1000
		},
		hide: {
			effect: "explode",
			duration: 1000
		}
	});

	$("#opener").click(function() {
		$("#dialog").dialog("open");
	});

	$('.formSaver').on('click', function() {
		$('.myTarget').text($('.myInput').val());
		$("#dialog").dialog('close');
	});
	
	$( "#spinner" ).spinner({min:0, max:5});
	
	
});