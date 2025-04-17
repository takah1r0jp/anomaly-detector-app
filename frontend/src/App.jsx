import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  return (
    <div className="app">
      {/* ヘッダー */}
      <header className="header">
        <h1>Zero-Shot AD</h1>
      </header>

      {/* 入力エリア */}
      <section className="input-section">

        <label htmlFor="normal">正常条件を入力して</label>
        <input type="text" id="normal" placeholder="入力してください" />

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
