import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import Landing from './components/Landing';
import Main from './components/Main'

import './App.css';
import './styles.css';
import 'bootstrap/dist/css/bootstrap.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Landing/>} />
          <Route path="/main" element={<Main/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
