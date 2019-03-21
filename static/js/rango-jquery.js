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
		height: 400,
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
		height: 350,
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
	}).css({ width: '234px', 'padding-top': '10px', 'padding-bottom': '10px' });

	
	$( "#myRating" ).spinner({min:0, max:5});
	
	$('.closeBtn').on('click', function() {
		$("#dialog").dialog('close');
	}).css({width: '30px'});

	$('#likes').on('click', function() {
		var deaid;
		deaid = $(this).attr("data-deaid");
		$.get('/meal_deal/like/', {deals_id: deaid}, function(data){ 
			$('#like_count').html(data);
				$('#likes').hide();
				$('#dislikes').hide();
		})
	}).css({ width: '115px', 'padding-top': '10px', 'padding-bottom': '10px' });
	
	$('#dislikes').on('click', function() {
		var deaid;
		deaid = $(this).attr("data-deaid");
		$.get('/meal_deal/dislike/', {deals_id: deaid}, function(data){ 
			$('#dislike_count').html(data);
				$('#likes').hide();
				$('#dislikes').hide();
		})
	}).css({ width: '115px', 'padding-top': '10px', 'padding-bottom': '10px' });
	
});