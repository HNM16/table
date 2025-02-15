import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "../style/App.css";
import Page from "../page.jsx/page.jsx";
// import Home from "../home/home.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
<Page/>
  </StrictMode>
);
