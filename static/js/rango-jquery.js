$(document).ready( function() {
	
	$("p").hover( function() {
		$(this).css('color', 'red');
	},

	function() {
		$(this).css('color', 'blue');
	});
	
	
	//Welcome dialog stuff
	
	$("#welcome").dialog({
		width: 400,
		height: 350,
		autoOpen: true,
		open: function(event, ui) { 
			jQuery('.ui-dialog-titlebar-close').hide();
		},
		show: {
			effect: "blind",
			duration: 1000
		},
		hide: {
			effect: "blind",
			duration: 1000
		}
	});
	
	$('.continueBtn').on('click', function() {
		$("#welcome").dialog('close');
	}).css({ width: '300px', 'padding-top': '10px', 'padding-bottom': '10px' });

	
	//Post review dialog stuff
	
	$("#dialog").dialog({
		width: 350,
		height: 300,
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
	}).css({ width: '300px', 'padding-top': '10px', 'padding-bottom': '10px' });

	$('.formSaver').on('click', function() {
		$('.myTarget').text($('.myComment').val());
		$("#dialog").dialog('close');
	}).css({ width: '230px', 'padding-top': '10px', 'padding-bottom': '10px' });
	
	$( "#myRating" ).spinner({min:0, max:5});
	
	$('.closeBtn').on('click', function() {
		$("#dialog").dialog('close');
	}).css({width: '70px', 'padding-top': '10px', 'padding-bottom': '10px' });
	
	
	
	$('#likes').click(function() {
		var catid;
		catid = $(this).attr("data-catid");
		$.get('/meal_deal/like/', {category_id: catid}, function(data){ 
			$('#like_count').html(data);
				$('#likes').hide();
		});
	});
	
});