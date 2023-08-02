$(function() {
	$('DIV#add_item').on('click', function() {
		$('UL.my_list').append('<li>Item</li>'); // Append the new element to the list
	});

	// Remove the last element when user clicks on DIV#remove_item
	$('DIV#remove_item').on('click', function() {
		$('UL.my_list li:last-child').remove(); // Remove the last <li> element from the list
	});

	// Clear all elements when user clicks on DIV#clear_list
	$('DIV#clear_list').on('click', function() {
		$('UL.my_list').empty(); // Remove all children from the list
	});
});
