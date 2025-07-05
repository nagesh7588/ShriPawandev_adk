class MLAgent:
    def run(self, context):
        try:
            print("🤖 Training machine learning model...")

            df = context.get("preprocessed_data")
            if df is None:
                raise ValueError("No preprocessed data found in context")

            target_column = "inj_person_count"

            if target_column not in df.columns:
                print(f"⚠️ '{target_column}' not found in columns. Available: {list(df.columns)}")
                raise ValueError(f"'{target_column}' column is missing.")

            # ✅ Drop rows where target is NaN
            df = df.dropna(subset=[target_column])

            # Separate X and y
            X = df.drop(columns=[target_column])
            y = df[target_column]

            # Only keep numeric columns in X
            X = X.select_dtypes(include="number").fillna(0)

            from sklearn.ensemble import RandomForestRegressor
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import mean_squared_error

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

            model = RandomForestRegressor()
            model.fit(X_train, y_train)

            preds = model.predict(X_test)
            mse = mean_squared_error(y_test, preds)

            print(f"✅ Model trained. MSE: {mse:.2f}")
            context["model"] = model
            return context

        except Exception as e:
            print(f"❌ Error: {e}")
            raise e
