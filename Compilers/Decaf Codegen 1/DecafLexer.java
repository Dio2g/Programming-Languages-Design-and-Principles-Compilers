// Generated from Decaf.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DecafLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		BOOLEAN=1, BREAK=2, CALLOUT=3, CLASS=4, CONTINUE=5, ELSE=6, FALSE=7, FOR=8, 
		IF=9, INT=10, RETURN=11, TRUE=12, VOID=13, LCURLY=14, RCURLY=15, LSQUARE=16, 
		RSQUARE=17, LBRACE=18, RBRACE=19, PLUS=20, MINUS=21, MULTIPLY=22, DIVIDE=23, 
		MOD=24, SEMICOLON=25, COMMA=26, EXCLAMATION=27, LESS_THAN=28, GREATER_THAN=29, 
		LESS_OR_EQUAL=30, GREATER_OR_EQUAL=31, DOUBLE_EQUAL=32, NOT_EQUAL=33, 
		AND=34, OR=35, ASSIGN=36, PLUS_ASSIGN=37, MINUS_ASSIGN=38, ID=39, DECIMAL_LITERAL=40, 
		HEX_LITERAL=41, WS=42, COMMENT=43, CHAR=44, STRING_LITERAL=45;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"BOOLEAN", "BREAK", "CALLOUT", "CLASS", "CONTINUE", "ELSE", "FALSE", 
			"FOR", "IF", "INT", "RETURN", "TRUE", "VOID", "LCURLY", "RCURLY", "LSQUARE", 
			"RSQUARE", "LBRACE", "RBRACE", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
			"MOD", "SEMICOLON", "COMMA", "EXCLAMATION", "LESS_THAN", "GREATER_THAN", 
			"LESS_OR_EQUAL", "GREATER_OR_EQUAL", "DOUBLE_EQUAL", "NOT_EQUAL", "AND", 
			"OR", "ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "ALPHA", "DIGIT", "ALPHA_NUM", 
			"ID", "DECIMAL_LITERAL", "HEX_DIGIT", "HEX_LITERAL", "WS", "COMMENT", 
			"BAD_CHARS", "DOUBLE_CHARS", "CHAR", "STRING_LITERAL"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'boolean'", "'break'", "'callout'", "'class'", "'continue'", "'else'", 
			"'false'", "'for'", "'if'", "'int'", "'return'", "'true'", "'void'", 
			"'{'", "'}'", "'['", "']'", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
			"'%'", "';'", "','", "'!'", "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", 
			"'&&'", "'||'", "'='", "'+='", "'-='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "BOOLEAN", "BREAK", "CALLOUT", "CLASS", "CONTINUE", "ELSE", "FALSE", 
			"FOR", "IF", "INT", "RETURN", "TRUE", "VOID", "LCURLY", "RCURLY", "LSQUARE", 
			"RSQUARE", "LBRACE", "RBRACE", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
			"MOD", "SEMICOLON", "COMMA", "EXCLAMATION", "LESS_THAN", "GREATER_THAN", 
			"LESS_OR_EQUAL", "GREATER_OR_EQUAL", "DOUBLE_EQUAL", "NOT_EQUAL", "AND", 
			"OR", "ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "ID", "DECIMAL_LITERAL", 
			"HEX_LITERAL", "WS", "COMMENT", "CHAR", "STRING_LITERAL"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public DecafLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Decaf.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2/\u0139\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3"+
		"\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r"+
		"\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3"+
		"\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3"+
		"\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3"+
		"\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'"+
		"\3\'\3\'\3(\3(\3)\3)\3*\3*\5*\u00f6\n*\3+\3+\7+\u00fa\n+\f+\16+\u00fd"+
		"\13+\3,\6,\u0100\n,\r,\16,\u0101\3-\3-\5-\u0106\n-\3.\3.\3.\3.\6.\u010c"+
		"\n.\r.\16.\u010d\3/\6/\u0111\n/\r/\16/\u0112\3/\3/\3\60\3\60\3\60\3\60"+
		"\7\60\u011b\n\60\f\60\16\60\u011e\13\60\3\60\3\60\3\60\3\60\3\61\3\61"+
		"\3\62\3\62\3\62\3\63\3\63\3\63\5\63\u012c\n\63\3\63\3\63\3\64\3\64\3\64"+
		"\7\64\u0133\n\64\f\64\16\64\u0136\13\64\3\64\3\64\2\2\65\3\3\5\4\7\5\t"+
		"\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23"+
		"%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G"+
		"%I&K\'M(O\2Q\2S\2U)W*Y\2[+],_-a\2c\2e.g/\3\2\t\5\2C\\aac|\3\2\62;\4\2"+
		"CHch\5\2\13\f\17\17\"\"\3\2\f\f\6\2\f\f$$))^^\6\2$$))^^pp\2\u013c\2\3"+
		"\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2"+
		"\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31"+
		"\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2"+
		"\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2"+
		"\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2"+
		"\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2"+
		"I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2[\3\2\2\2\2]\3"+
		"\2\2\2\2_\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\3i\3\2\2\2\5q\3\2\2\2\7w\3\2\2"+
		"\2\t\177\3\2\2\2\13\u0085\3\2\2\2\r\u008e\3\2\2\2\17\u0093\3\2\2\2\21"+
		"\u0099\3\2\2\2\23\u009d\3\2\2\2\25\u00a0\3\2\2\2\27\u00a4\3\2\2\2\31\u00ab"+
		"\3\2\2\2\33\u00b0\3\2\2\2\35\u00b5\3\2\2\2\37\u00b7\3\2\2\2!\u00b9\3\2"+
		"\2\2#\u00bb\3\2\2\2%\u00bd\3\2\2\2\'\u00bf\3\2\2\2)\u00c1\3\2\2\2+\u00c3"+
		"\3\2\2\2-\u00c5\3\2\2\2/\u00c7\3\2\2\2\61\u00c9\3\2\2\2\63\u00cb\3\2\2"+
		"\2\65\u00cd\3\2\2\2\67\u00cf\3\2\2\29\u00d1\3\2\2\2;\u00d3\3\2\2\2=\u00d5"+
		"\3\2\2\2?\u00d8\3\2\2\2A\u00db\3\2\2\2C\u00de\3\2\2\2E\u00e1\3\2\2\2G"+
		"\u00e4\3\2\2\2I\u00e7\3\2\2\2K\u00e9\3\2\2\2M\u00ec\3\2\2\2O\u00ef\3\2"+
		"\2\2Q\u00f1\3\2\2\2S\u00f5\3\2\2\2U\u00f7\3\2\2\2W\u00ff\3\2\2\2Y\u0105"+
		"\3\2\2\2[\u0107\3\2\2\2]\u0110\3\2\2\2_\u0116\3\2\2\2a\u0123\3\2\2\2c"+
		"\u0125\3\2\2\2e\u0128\3\2\2\2g\u012f\3\2\2\2ij\7d\2\2jk\7q\2\2kl\7q\2"+
		"\2lm\7n\2\2mn\7g\2\2no\7c\2\2op\7p\2\2p\4\3\2\2\2qr\7d\2\2rs\7t\2\2st"+
		"\7g\2\2tu\7c\2\2uv\7m\2\2v\6\3\2\2\2wx\7e\2\2xy\7c\2\2yz\7n\2\2z{\7n\2"+
		"\2{|\7q\2\2|}\7w\2\2}~\7v\2\2~\b\3\2\2\2\177\u0080\7e\2\2\u0080\u0081"+
		"\7n\2\2\u0081\u0082\7c\2\2\u0082\u0083\7u\2\2\u0083\u0084\7u\2\2\u0084"+
		"\n\3\2\2\2\u0085\u0086\7e\2\2\u0086\u0087\7q\2\2\u0087\u0088\7p\2\2\u0088"+
		"\u0089\7v\2\2\u0089\u008a\7k\2\2\u008a\u008b\7p\2\2\u008b\u008c\7w\2\2"+
		"\u008c\u008d\7g\2\2\u008d\f\3\2\2\2\u008e\u008f\7g\2\2\u008f\u0090\7n"+
		"\2\2\u0090\u0091\7u\2\2\u0091\u0092\7g\2\2\u0092\16\3\2\2\2\u0093\u0094"+
		"\7h\2\2\u0094\u0095\7c\2\2\u0095\u0096\7n\2\2\u0096\u0097\7u\2\2\u0097"+
		"\u0098\7g\2\2\u0098\20\3\2\2\2\u0099\u009a\7h\2\2\u009a\u009b\7q\2\2\u009b"+
		"\u009c\7t\2\2\u009c\22\3\2\2\2\u009d\u009e\7k\2\2\u009e\u009f\7h\2\2\u009f"+
		"\24\3\2\2\2\u00a0\u00a1\7k\2\2\u00a1\u00a2\7p\2\2\u00a2\u00a3\7v\2\2\u00a3"+
		"\26\3\2\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7\7v\2\2\u00a7"+
		"\u00a8\7w\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa\7p\2\2\u00aa\30\3\2\2\2\u00ab"+
		"\u00ac\7v\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af\7g\2\2"+
		"\u00af\32\3\2\2\2\u00b0\u00b1\7x\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3\7"+
		"k\2\2\u00b3\u00b4\7f\2\2\u00b4\34\3\2\2\2\u00b5\u00b6\7}\2\2\u00b6\36"+
		"\3\2\2\2\u00b7\u00b8\7\177\2\2\u00b8 \3\2\2\2\u00b9\u00ba\7]\2\2\u00ba"+
		"\"\3\2\2\2\u00bb\u00bc\7_\2\2\u00bc$\3\2\2\2\u00bd\u00be\7*\2\2\u00be"+
		"&\3\2\2\2\u00bf\u00c0\7+\2\2\u00c0(\3\2\2\2\u00c1\u00c2\7-\2\2\u00c2*"+
		"\3\2\2\2\u00c3\u00c4\7/\2\2\u00c4,\3\2\2\2\u00c5\u00c6\7,\2\2\u00c6.\3"+
		"\2\2\2\u00c7\u00c8\7\61\2\2\u00c8\60\3\2\2\2\u00c9\u00ca\7\'\2\2\u00ca"+
		"\62\3\2\2\2\u00cb\u00cc\7=\2\2\u00cc\64\3\2\2\2\u00cd\u00ce\7.\2\2\u00ce"+
		"\66\3\2\2\2\u00cf\u00d0\7#\2\2\u00d08\3\2\2\2\u00d1\u00d2\7>\2\2\u00d2"+
		":\3\2\2\2\u00d3\u00d4\7@\2\2\u00d4<\3\2\2\2\u00d5\u00d6\7>\2\2\u00d6\u00d7"+
		"\7?\2\2\u00d7>\3\2\2\2\u00d8\u00d9\7@\2\2\u00d9\u00da\7?\2\2\u00da@\3"+
		"\2\2\2\u00db\u00dc\7?\2\2\u00dc\u00dd\7?\2\2\u00ddB\3\2\2\2\u00de\u00df"+
		"\7#\2\2\u00df\u00e0\7?\2\2\u00e0D\3\2\2\2\u00e1\u00e2\7(\2\2\u00e2\u00e3"+
		"\7(\2\2\u00e3F\3\2\2\2\u00e4\u00e5\7~\2\2\u00e5\u00e6\7~\2\2\u00e6H\3"+
		"\2\2\2\u00e7\u00e8\7?\2\2\u00e8J\3\2\2\2\u00e9\u00ea\7-\2\2\u00ea\u00eb"+
		"\7?\2\2\u00ebL\3\2\2\2\u00ec\u00ed\7/\2\2\u00ed\u00ee\7?\2\2\u00eeN\3"+
		"\2\2\2\u00ef\u00f0\t\2\2\2\u00f0P\3\2\2\2\u00f1\u00f2\t\3\2\2\u00f2R\3"+
		"\2\2\2\u00f3\u00f6\5O(\2\u00f4\u00f6\5Q)\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4"+
		"\3\2\2\2\u00f6T\3\2\2\2\u00f7\u00fb\5O(\2\u00f8\u00fa\5S*\2\u00f9\u00f8"+
		"\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc"+
		"V\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u0100\5Q)\2\u00ff\u00fe\3\2\2\2\u0100"+
		"\u0101\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102X\3\2\2\2"+
		"\u0103\u0106\5Q)\2\u0104\u0106\t\4\2\2\u0105\u0103\3\2\2\2\u0105\u0104"+
		"\3\2\2\2\u0106Z\3\2\2\2\u0107\u0108\7\62\2\2\u0108\u0109\7z\2\2\u0109"+
		"\u010b\3\2\2\2\u010a\u010c\5Y-\2\u010b\u010a\3\2\2\2\u010c\u010d\3\2\2"+
		"\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\\\3\2\2\2\u010f\u0111"+
		"\t\5\2\2\u0110\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0110\3\2\2\2\u0112"+
		"\u0113\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\b/\2\2\u0115^\3\2\2\2\u0116"+
		"\u0117\7\61\2\2\u0117\u0118\7\61\2\2\u0118\u011c\3\2\2\2\u0119\u011b\n"+
		"\6\2\2\u011a\u0119\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011c"+
		"\u011d\3\2\2\2\u011d\u011f\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0120\7\f"+
		"\2\2\u0120\u0121\3\2\2\2\u0121\u0122\b\60\2\2\u0122`\3\2\2\2\u0123\u0124"+
		"\n\7\2\2\u0124b\3\2\2\2\u0125\u0126\7^\2\2\u0126\u0127\t\b\2\2\u0127d"+
		"\3\2\2\2\u0128\u012b\7)\2\2\u0129\u012c\5a\61\2\u012a\u012c\5c\62\2\u012b"+
		"\u0129\3\2\2\2\u012b\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012e\7)"+
		"\2\2\u012ef\3\2\2\2\u012f\u0134\7$\2\2\u0130\u0133\5a\61\2\u0131\u0133"+
		"\5c\62\2\u0132\u0130\3\2\2\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2\u0134"+
		"\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0137\3\2\2\2\u0136\u0134\3\2"+
		"\2\2\u0137\u0138\7$\2\2\u0138h\3\2\2\2\r\2\u00f5\u00fb\u0101\u0105\u010d"+
		"\u0112\u011c\u012b\u0132\u0134\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}