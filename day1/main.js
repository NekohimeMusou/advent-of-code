window.onload = function() {
    // Trim whitespace off the list and convert to numbers
    let input = get_input().map((item => Number(item.trim())));

    let part_2_result = calc_part_2(input);
};

function get_input() {
    return document.getElementById("input_elem").textContent;
}

function calc_part_2(numbers) {
    
}