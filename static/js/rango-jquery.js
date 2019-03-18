$(document).ready( function() {
	
	$("p").hover( function() {
		$(this).css('color', 'red');
	},

	function() {
		$(this).css('color', 'blue');
	});

	$("#dialog").dialog({
		width: 350,
		height: 250,
		autoOpen: false,
		open: function(event, ui) { 
			jQuery('.ui-dialog-titlebar-close').hide(); 
			jQuery('#myComment').val('');
			jQuery('#myRating').val('');
		},
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
		$('.myTarget').text($('.myComment').val());
		$("#dialog").dialog('close');
	});
	
	$( "#myRating" ).spinner({min:0, max:5});
	
	
});