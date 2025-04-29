import { useState, useRef } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const conditionRef = useRef();
  const [normalcondition, setCondition] = useState(["There are two apples."]);

  const handleAddCondition = () => {
    const condition = conditionRef.current.value;
    if (condition) {
      setCondition([...normalcondition, condition]);

      conditionRef.current.value = null;
    }
  };
  
  return (
    <div className="app">
      {/* ヘッダー */}
      <header className="header">
        <h1>Zero-Shot AD</h1>
      </header>

      {/* 入力エリア */}
      <section className="input-section">

        <label htmlFor="normal">正常条件を入力してください</label>

        <div className="input-with-button">
          <input type="text" id="normal" placeholder="入力してください" ref={conditionRef}  />
          <button onClick={handleAddCondition}>追加</button>
        </div>

        {/* 追加された正常条件の表示 */}
        <div className="condition-list">
          <h3>追加された正常条件：</h3>
          {normalcondition.length > 0 ? (
            <ul>
              {normalcondition.map((condition, index) => (
                <li key={index}>{condition}</li>
              ))}
            </ul>
          ) : (
            <p>まだ条件が追加されていません</p>
          )
          } 
        </div>

        <label htmlFor="image">異常検知画像</label>
        <div className="image-box">ここに画像</div>
      </section>

      {/* 結果表示エリア */}
      <section className="result-section">
        <label>異常検知結果</label>
        <div className="image-box">ここに異常検知結果</div>
      </section>
    </div>
  );
}

export default App
