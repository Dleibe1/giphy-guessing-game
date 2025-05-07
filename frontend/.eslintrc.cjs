module.exports = {
	extends: [
	  "airbnb",
	  "airbnb/hooks",
	  "plugin:@typescript-eslint/recommended",
	  "prettier"
	],
	parser: "@typescript-eslint/parser",
	parserOptions: {
	  ecmaVersion: 2021,
	  sourceType: "module",
	  project: "./tsconfig.json",
	  ecmaFeatures: {
		jsx: true
	  }
	},
	plugins: [
	  "react", 
	  "react-hooks", 
	  "@typescript-eslint",
	  "prettier" 
	],
	settings: {
	  react: {
		version: "detect"
	  }
	},
	rules: {
	  "indent": ["error", 2],
	  "react/jsx-filename-extension": [1, { "extensions": [".tsx", ".jsx"] }],
	  "import/extensions": [
		"error",
		"ignorePackages",
		{
		  "js": "never",
		  "jsx": "never",
		  "ts": "never",
		  "tsx": "never"
		}
	  ],
	  "prettier/prettier": "error",
	}
  };