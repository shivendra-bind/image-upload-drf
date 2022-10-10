import { useState } from "react";
import "./App.css";

function App() {
  const [image, setImage] = useState<File>();
  const [url, seUrl] = useState("");
  const onSubmit = async (
    evt: React.MouseEvent<HTMLButtonElement, MouseEvent>
  ) => {
    evt.preventDefault();
    if (image) {
      const formData = new FormData();
      formData.append("image", image, image?.name);
      const response = await fetch("http://localhost:8000/upload/", {
        method: "POST",
        body: formData,
      });
      const result = await response.json();
      const { url } = result;
      seUrl(url);
    }
  };
  return (
    <div className="App">
      <div className="card">
        <p className="read-the-docs">Upload image</p>
        <div className="input__wrapper">
          <label className="input__label" htmlFor="file-input">
            Upload Image
          </label>
          <input
            id="file-input"
            type="file"
            accept=""
            className="input__input"
            onChange={(e) => e.target?.files && setImage(e.target.files[0])}
          />
        </div>
        <button onClick={(e) => onSubmit(e)}>Upload</button>
      </div>
      <div>{url && <img className="image" src={url} alt="" />}</div>
    </div>
  );
}

export default App;
