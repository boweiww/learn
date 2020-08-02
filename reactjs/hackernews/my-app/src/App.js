import React, { Component } from 'react';
import './App.css';
const JsonTable = require('ts-react-json-table');

class App extends Component {
    constructor(props) {
    super(props);
    this.state = {
      data: null,
      columns: null,
      content: null,
      page: 0
    };
    this.onSearchChange = this.onSearchChange.bind(this);
    this.onSearchSubmit = this.onSearchSubmit.bind(this);
    this.onNextpage = this.onNextpage.bind(this);
    this.onPreviouspage = this.onPreviouspage.bind(this);
  }
// state = {
//     data: null,
//     columns: null,
//     content: null
//   };

  componentDidMount() {
    // const value = this.state.content;
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ content: 'news' , type: 'news',page: this.state.page})
  };
  // fetch('/express_backend');
  fetch('http://localhost:5000/express_backend', requestOptions)
      .then(response => response.json())
      .then(data => this.processJson(data));
  
  } 


  processJson(datas){
    datas.sort(function(a, b) {
      return a.objectID - b.objectID;
  });
      var columns = [
        'objectID',
      'title',
      'url',
      'author'
  ];
    // console.log(datas);
    this.setState({ data: datas,columns:columns});
    
  }
  searchValue(value){
    var searchtype;
    if (value == null){
      searchtype = 'news';
    }
    else{
      searchtype = 'search';
    }
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ content: value , type: searchtype,page: this.state.page})
  };
  // fetch('/express_backend');
  fetch('http://localhost:5000/express_backend', requestOptions)
      .then(response => response.json())
      .then(data => this.processJson(data));
  }
  onClickCell(event, columnName, rowData){
    console.log(rowData.url);
    if (rowData.url != null){
      window.location.href = rowData.url; 

    }

  }
  onSearchChange(event) {
    this.setState({ content: event.target.value,page:0});
    this.searchValue(this.state.content);
  }
  onSearchSubmit(){
    // this.state.page = 0;
    this.searchValue(this.state.content);

  }
  onPreviouspage(){
    if (this.state.page > 0){
      // this.state.page = this.state.page - 1;
      this.setState({ page:this.state.page - 1});
      this.searchValue(this.state.content);

    }
    
  }
  onNextpage(){
    // this.state.page = this.state.page + 1;
    this.setState({ page:this.state.page + 1});
    this.searchValue(this.state.content);
    
  }

  render() {
    return (
      
      <div className="App">
        <div className="interactions">
          
          <input type='text' id="input"  placeholder="Search Here" onChange={this.onSearchChange}/>

        </div>

        <JsonTable rows={this.state.data} columns={this.state.columns} onClickCell={ this.onClickCell }/>
        <button  id="changePage" onClick={this.onPreviouspage}>Previous</button>
        <h2 id="pageNum">  {this.state.page + 1}  </h2>
        <button  id="changePage" onClick={this.onNextpage}>next</button>

      </div>
    );
  }
}

export default App;