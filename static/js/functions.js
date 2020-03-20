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

// Listen changes in <select>
$(document).ready(function() {
    var previous_value;

    $("select").on('focus', function () {
        // Store the current value on focus and on change
        previous_value = this.value;
    }).change(function() {
        should_enable_submit('form-control');
        dropOthersValues(this, previous_value);
    });
})();


// Check duplicate order values
function dropOthersValues(select, previous_value) {
    actual_value = getOption(select.id)

    if(actual_value){
        removeOption(select.id, actual_value);
        addOption(select.id, actual_value, previous_value);
    }
}

function getOption(select_id){
    var select = document.getElementById(select_id);
    if(select.options.length > 0) {
        return select.value;
    }
    return false;
}


function addOption(select_id, actual_value, previous_value){
    var selects = document.getElementsByTagName('select');
    for(i=0; i<selects.length; i++) {
        if(selects[i].id === select_id) continue;

        for(k=0; k<selects[i].length; k++){
            if(selects[i].options[k].value === previous_value)
                return false;
        }

        // create new option element
        var opt = document.createElement('option');
        // create text node to add to option element (opt)
        opt.appendChild( document.createTextNode(previous_value) );
        // set value property of opt
        opt.value = previous_value;
        // add opt to end of select box (sel)
        selects[i].appendChild(opt);

    }
}

function removeOption(select_id, actual_value){
    var selects = document.getElementsByTagName('select');
    for(i=0; i<selects.length; i++) {
        if(selects[i].id === select_id) continue;
        for(k=1; k<selects[i].length; k++){
            if(selects[i].options[k].value === actual_value)
                selects[i].options[k] = null;
        }
    }
}

