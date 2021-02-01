
function display_meta_data(entry) {
  return `
    <div class="entrydata">
    <h4 class="headers">META DATA</h4> 
    <p class="attributes">timestamp: ${entry.meta_data.timestamp} </p>
    <p class="attributes">public_key: ${entry.meta_data.public_key} </p>
    <p class="attributes">signature: ${entry.meta_data.signature} </p>
  
    </div>
  `;
}
//<img class="pet-photo" src="https://learnwebcode.github.io/json-example/images/cat-1.jpg">
function display_entry(entry_object) {

    if (entry_object.meta_data.entry_type === "genesis"){

        return `<div class="entry">
            <p class="headers">GENESIS</p> </div>`;
    }

    if (entry_object.meta_data.entry_type === "uni"){
          return `
            <div class="entry">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">NAME: ${entry_object.entry_data.name} </p> 
                        <p class="attributes">ID: ${entry_object.entry_data.uni_id} </p> 
                        </div>
            ${display_meta_data(entry_object)}</div>`;

    }
    if (entry_object.meta_data.entry_type === "uni_key"){
          return `
            <div class="entry">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">UNI: ${entry_object.entry_data.uni_id} </p> 
                        <p class="attributes">KEY: ${entry_object.entry_data.key} </p> 
                        </div>
            ${display_meta_data(entry_object)} </div>`;

    }

    if (entry_object.meta_data.entry_type === "admin_key"){
          return `
            <div class="entry">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">KEY: ${entry_object.entry_data.key} </p> 
                        </div>
            ${display_meta_data(entry_object)}</div>`;

    }

    if (entry_object.meta_data.entry_type === "revoke_key"){
          return `
            <div class="entry">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">KEY: ${entry_object.entry_data.key} </p> 
                        </div>
            ${display_meta_data(entry_object)} </div>`;

    }

    if (entry_object.meta_data.entry_type === "subject"){
          return `
            <div class="entry">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">NAME: ${entry_object.entry_data.name} </p> 
                        <p class="attributes">UNI: ${entry_object.entry_data.uni_id} </p> 
                        <p class="attributes">ID: ${entry_object.entry_data.subject_id} </p>
                        </div> 
            ${display_meta_data(entry_object)} </div>`;

    }
    if (entry_object.meta_data.entry_type === "student"){
          return `
            <div class="entry">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">NAME: ${entry_object.entry_data.name} </p> 
                        <p class="attributes">ID: ${entry_object.entry_data.student_id} </p>  
                        </div>
            ${display_meta_data(entry_object)} </div>`;

    }
    if (entry_object.meta_data.entry_type === "matriculation"){
          return `
            <div class="entry">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">UNI: ${entry_object.entry_data.uni_id} </p> 
                        <p class="attributes">MATRICLE NUMBER: ${entry_object.entry_data.m_number} </p> 
                        </div>
            ${display_meta_data(entry_object)} </div>`;

    }
    if (entry_object.meta_data.entry_type === "exmatriculation"){
          return `
            <div class="entry">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">UNI: ${entry_object.entry_data.uni_id} </p> 
                        <p class="attributes">MATRICLE NUMBER: ${entry_object.entry_data.m_number} </p> 
                        </div>
            ${display_meta_data(entry_object)}</div>`;

    }
    if (entry_object.meta_data.entry_type === "exam"){
          return `
            <div class="entry">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">NAME: ${entry_object.entry_data.name} </p> 
                        <p class="attributes">UNI: ${entry_object.entry_data.uni_id} </p> 
                        <p class="attributes">EXAM: ${entry_object.entry_data.exam_id} </p> 
                        <p class="attributes">SUBJECT: ${entry_object.entry_data.subject_id} </p> 
                        </div>
            ${display_meta_data(entry_object)} </div>`;

    }
    if (entry_object.meta_data.entry_type === "cancel"){
          return `
            <div class="entry">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">CANCELED ENTRY: ${entry_object.entry_data.canceled_entry_id} </p> 
                        </div>
            ${display_meta_data(entry_object)} </div>`;

    }
    if (entry_object.meta_data.entry_type === "attempt"){
          return `
            <div class="entry">
            <h4 class="headers">${entry_object.entry_id} - ${entry_object.meta_data.entry_type}</h4> 
            <div class="entrydata">
            <h4 class="headers">ENTRY DATA</h4> 
                        <p class="attributes">UNI: ${entry_object.entry_data.uni_id} </p> 
                        <p class="attributes">MATRICLE NUMBER: ${entry_object.entry_data.m_number} </p>
                        <p class="attributes">EXAM: ${entry_object.entry_data.exam_id} </p>
                        <p class="attributes">GRADE: ${entry_object.entry_data.grade} </p>
                        </div>
                            ${display_meta_data(entry_object)} </div>`;

    }

}







function display_block(block) {
  return `
    <div class="block">
    <p class="attributes">timestamp: ${block.timestamp} </p>
    <p class="attributes">difficulty: ${block.difficulty} </p>
    <p class="attributes">nonce: ${block.nonce} </p>
    <p class = "attributes">last_hash: </strong> ${block.last_hash}</p>
    <p class = "attributes">hash: </strong> ${block.hash}</p>
    <h4 class="headers">${block.data.length} Entrie/s</h4>
        <div class="entries">
        ${block.data.map(entry_o => display_entry(entry_o)).join("")}
        </div>
    </div>
  `;
}


var targetContainer = document.getElementById("app");
var eventSource = new EventSource("/stream/blockchain")
mem = null
eventSource.onmessage = function(e) {
    //console.log(e.data);
    if (e.data === mem){
        return
    }
    mem = e.data;
    ne = e.data.replace(/'/g, '"');
    jsonobj = JSON.parse(ne);
    targetContainer.innerHTML =`
      <h1 class="app-title">Blockchain (${jsonobj.length} Block/s)</h1>
      ${jsonobj.map(display_block).join("")}
    `;
};