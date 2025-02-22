import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Upload from './components/Upload';
import Home from './components/Home';
import Chat from './components/Chat'
import Navbar from './components/Navbar';
function App() {
  return (
    <>
      <Router>
        <Navbar/>
        <Routes>
          <Route path='/' element={<Home/>} />
          <Route path='/upload' element={<Upload/>} />
          <Route path='/upload' element={<Upload/>} />
          <Route path='/chat' element={<Chat/>} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
