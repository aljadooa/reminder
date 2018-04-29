$(document).ready(function() {

    // edit a reminder
    $(".update-btn").on("click", function() {
        let id = this.id,
            dashboardURL = 'http://' + window.location.host + '/dashboard', 
            windowURL = window.location.href

        let reminder = {
            "title": $("#title-" + id).val(),
            "reminder": $("#reminder-" + id).val(),
            "date": $("#date-" + id).val()
        }

        // feed reminder data to modal
        $("#modal-edit").on("show.bs.modal", function(event) {

            // set the form's "action" attribute with the right destination 
            if(dashboardURL != windowURL) {
                document.getElementById("edit-form").action = "update?id=" + id
            }else if (dashboardURL == windowURL) {
                document.getElementById("edit-form").action = "r/update?id=" + id
            }
            
            // using this because jquery selectors didn"t work :/
            document.getElementById("edit-title").value = reminder["title"]
            CKEDITOR.instances["edit-reminder"].setData(reminder["reminder"]);
            document.getElementById("edit-date").value = reminder["date"]
        });

        // toggle edit modal
        $("#modal-edit").modal("show");

    }); // update reminder

    $(".delete-btn").on("click", function() {
        let id = this.id

        axios.post('/r/delete?id=' + id).then(function(response) {

            let reminder = document.getElementById("r-" + id);
            reminder.outerHTML = "";
            delete reminder;

            console.log(response.message);
        }).catch(function(error) {
            console.error(error)
        });
    }); // delete reminder

    $(".check-complete").change(function() {

        let id = this.id

        const isChecked = $(this).prop('checked'),
              completed = $("#completed-" + id);


        if (isChecked) {
            axios.post('/r/complete?id=' + id).then(function(response) {
                console.log(response.result);
            }).catch(function(error) {
                console.error(error);
            });

            completed.empty();
            completed.append("Yes");

        } else {
            axios.post('/r/uncomplete?id=' + id).then(function(response) {
                console.log(response.result);
            }).catch(function(error) {
                console.error(error);
            });

            completed.empty();
            completed.append("No");
        }
    }); // complete/uncomplete a reminder
});