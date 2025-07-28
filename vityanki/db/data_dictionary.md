## Table: users

Stores information about bot users and their preferences (settings).

| Column             | Type       | Nullable | Default | Description                                 |
|--------------------|------------|----------|---------|---------------------------------------------|
| telegram_id        | BigInteger | No       | —       | Unique Telegram user ID (primary key)       |
| interface_language | String(8)  | No       | "en"    | Language code for the user's UI preference  |
