// Enable submit buttton
function should_enable_submit(element_class){
    elements = document.getElementsByClassName(element_class);
    for(var i=0; i<elements.length; i++) {
        // First <option> value of a table row
        value = elements[i].options[elements[i].selectedIndex].value[0];
//        console.log(value)
        if (value === '0')
            return false;
    }
    enable_submit_button("btn-submit");
    return true;
}

function enable_submit_button(button_id){
    document.getElementById(button_id).disabled = false;
}

// Input value in <option> element
function setInputValue(input_id, option_selected) {
    document.getElementById(input_id).setAttribute('value', option_selected.value);
}

// Check duplicate order values
function dropOthersValues() {
    var selects = document.getElementsByTagName('select');
    var values = [];
    for(i=0;i<selects.length;i++) {
        var select = selects[i];
        if(values.indexOf(select.value)>-1 && select.value > 0) {
            alert('Verifique a seguinte ordem duplicada: '+ select.value); break;
        }
        else
            values.push(select.value);
    }
}
