function showType(fileInput) {
    const files = fileInput.files;
  
    for (const i = 0; i < files.length; i++) {
      const name = files[i].name;
      const type = files[i].type;
      alert("Filename: " + name + " , Type: " + type);
    }
  }