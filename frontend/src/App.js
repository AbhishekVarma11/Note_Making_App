import Header from './components/Header'
import { HashRouter as Router,Route ,Routes } from 'react-router-dom'; //use HashRouter instead of BrowserRouter for refresh with integrating with Django
import './App.css';
import NotePage from './components/NotePage';
import NotesListPage from './pages/NotesListPage'
function App() {
  return (
    <div className='container dark'>
    <div className='app'>
    <Header/>
    <Router>
    <Routes>

  
    <Route path="/" exact Component={NotesListPage}/>
    <Route path="/note/:id" Component={NotePage}/>

    </Routes>
</Router>
    </div>
    </div>
  );
}

export default App;
