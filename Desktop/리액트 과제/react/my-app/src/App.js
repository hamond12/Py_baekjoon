import './App.css';
import React ,{Component} from 'react';

  export default class App extends Component {

    constructor(props) {
      super(props);

      this.state = {
        text: "빈 방",
      };
    }

    changeText = () => {
      this.setState({
        text: "예약 됨",
      });
    };

    render(){
      return(
      <div className="App">
        <h1>교실 예약 프로그램</h1>
        <table>
          <tr>
            <th>
              2-1 <div><button id="btn" onClick={this.changeText}>예약</button><h6>{this.state.text}</h6></div>
            </th>
            <th>
              2-2 <div><button id="btn" onClick={this.changeText}>예약</button><h6>{this.state.text}</h6></div>
            </th>
            <th>
              2-3 <div><button id="btn" onClick={this.changeText}>예약</button><h6>{this.state.text}</h6></div>
            </th>
            <th>
              2-4 <div><button id="btn" onClick={this.changeText}>예약</button><h6>{this.state.text}</h6></div>
           </th>
          </tr>
        </table>
      </div>
    );
  }
}