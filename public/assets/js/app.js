$(document).ready(function () {
    
    // edit a reminder
    $(".update-btn").on("click", function () {
       let id = this.id
        
       let reminder = {
           "title": $("#title-"+id).val(),
           "reminder": $("#reminder-"+id).val(),
           "date": $("#date-"+id).val()
       }

       // feed reminder data to modal
       $("#modal-edit").on("show.bs.modal", function (event) {
            
            // set the form's "action" attribute with the right destination 
            document.getElementById("edit-form").action = "r/update?id="+id
            // using this because jquery selectors didn"t work :/
            document.getElementById("edit-title").value = reminder["title"]
            CKEDITOR.instances["edit-reminder"].setData(reminder["reminder"]);
            document.getElementById("edit-date").value = reminder["date"]
       });

       // toggle edit modal
       $("#modal-edit").modal("show");

    });

    // delete reminder
    $(".delete-btn").on("click", function () {
        let id = this.id
        
        axios.post('/r/delete?id='+id).then(function(response){
        
            let reminder = document.getElementById("r-"+id);
            reminder.outerHTML = "";
            delete reminder;

            console.log(response.message);
        }).catch(function(error){
            console.error(error)
        })
    });
});

// filter out html
function filter(input) {
    let result = jQuery(input).text()

    return result
}
