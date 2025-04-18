## 技術構成と選定理由

本アプリケーションは、画像の異常検知をゼロショットで行うことを目的とし、フロントエンド・バックエンドの構成を明確に分離して設計しています。以下に主要技術とその選定理由を記載します。

---

### フロントエンド


---

### バックエンド

- **FastAPI**
  - 高速なAPI開発が可能なPython製フレームワーク。型ヒントや自動ドキュメント生成にも対応しています。
- **Python**
  - 研究における既存の資産（画像処理やモデル）を活かしやすく、深層学習との相性が良好です。
- **PyTorch**
  - ゼロショット異常検知などの実装において柔軟かつ扱いやすく、研究コードをそのままAPI化できます。
- **基盤モデル（例：CLIP）**
  - テキスト条件に基づく画像理解が可能で、ユーザーの入力とモデルを自然に接続できるゼロショットアプローチを採用しています。

---

### インフラ・開発環境

- **GitHub**
  - バージョン管理とチーム開発に対応し、成果物を公開することでポートフォリオとしても活用可能です。
- **研究室PC（GPU搭載）**
  - モデル推論をリアルタイムに実行できるハードウェア環境を活かし、開発効率と応答速度の向上を図っています。
- **ローカル環境 + ngrok（必要に応じて）**
  - ローカルでの動作確認から、外部アクセス可能な簡易公開までスムーズに対応できます。

---

### 設計方針

- フロントエンドとバックエンドを分離し、開発とデプロイの自由度を高めました。
- 研究資産の有効活用と再利用性を意識し、バックエンドはFastAPI + Pythonで構成。
