function display_entry_3(entry_object) {

    if (entry_object.meta_data.entry_type === "genesis"){

        return `<div class="entry-pool">
            <p class="headers">GENESIS</p> </div>`;
    }

    if (entry_object.meta_data.entry_type === "uni"){
          return `
            <div class="entry-pool">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata-pool">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">NAME: ${entry_object.entry_data.name} </p> 
                        <p class="attributes">ID: ${entry_object.entry_data.uni_id} </p> 
                        </div></div>`;

    }
    if (entry_object.meta_data.entry_type === "uni_key"){
          return `
            <div class="entry-pool">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata-pool">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">UNI: ${entry_object.entry_data.uni_id} </p> 
                        <p class="attributes">KEY: ${entry_object.entry_data.key} </p> 
                        </div> </div>`;

    }

    if (entry_object.meta_data.entry_type === "admin_key"){
          return `
            <div class="entry-pool">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata-pool">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">KEY: ${entry_object.entry_data.key} </p> 
                        </div></div>`;

    }

    if (entry_object.meta_data.entry_type === "revoke_key"){
          return `
            <div class="entry-pool">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata-pool">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">KEY: ${entry_object.entry_data.key} </p> 
                        </div> </div>`;

    }

    if (entry_object.meta_data.entry_type === "subject"){
          return `
            <div class="entry-pool">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata-pool">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">NAME: ${entry_object.entry_data.name} </p> 
                        <p class="attributes">UNI: ${entry_object.entry_data.uni_id} </p> 
                        <p class="attributes">ID: ${entry_object.entry_data.subject_id} </p>
                        </div> </div>`;

    }
    if (entry_object.meta_data.entry_type === "student"){
          return `
            <div class="entry-pool">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata-pool">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">NAME: ${entry_object.entry_data.name} </p> 
                        <p class="attributes">ID: ${entry_object.entry_data.student_id} </p>  
                        </div></div>`;

    }
    if (entry_object.meta_data.entry_type === "matriculation"){
          return `
            <div class="entry-pool">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata-pool">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">UNI: ${entry_object.entry_data.uni_id} </p> 
                        <p class="attributes">MATRICLE NUMBER: ${entry_object.entry_data.m_number} </p> 
                        </div></div>`;

    }
    if (entry_object.meta_data.entry_type === "exmatriculation"){
          return `
            <div class="entry-pool">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata-pool">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">UNI: ${entry_object.entry_data.uni_id} </p> 
                        <p class="attributes">MATRICLE NUMBER: ${entry_object.entry_data.m_number} </p> 
                        </div> </div>`;

    }
    if (entry_object.meta_data.entry_type === "exam"){
          return `
            <div class="entry-pool">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata-pool">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">NAME: ${entry_object.entry_data.name} </p> 
                        <p class="attributes">UNI: ${entry_object.entry_data.uni_id} </p> 
                        <p class="attributes">EXAM: ${entry_object.entry_data.exam_id} </p> 
                        <p class="attributes">SUBJECT: ${entry_object.entry_data.subject_id} </p> 
                        </div> </div>`;

    }
    if (entry_object.meta_data.entry_type === "cancel"){
          return `
            <div class="entry-pool">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata-pool">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">CANCELED ENTRY: ${entry_object.entry_data.canceled_entry_id} </p> 
                        </div> </div>`;

    }
    if (entry_object.meta_data.entry_type === "attempt"){
          return `
            <div class="entry-pool">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata-pool">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">UNI: ${entry_object.entry_data.uni_id} </p> 
                        <p class="attributes">MATRICLE NUMBER: ${entry_object.entry_data.m_number} </p>
                        <p class="attributes">EXAM: ${entry_object.entry_data.exam_id} </p>
                        <p class="attributes">GRADE: ${entry_object.entry_data.grade} </p>
                        </div></div>`;

    }

}

