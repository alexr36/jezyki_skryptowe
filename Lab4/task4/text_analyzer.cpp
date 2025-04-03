#include <iostream>
#include <fstream>
#include <sstream>
#include <unordered_map>


// A structure to contain info about analyzed text
struct TextFileStats {
    std::string filepath;
    size_t chars_count = 0;
    size_t words_count = 0;
    size_t lines_count = 0;
    char most_common_char = '\0';
    std::string most_common_word;
};



std::vector<std::string> read_lines(const std::string &filepath) {
    std::ifstream file(filepath);
    std::vector<std::string> lines;

    if (!file.is_open()) {
        std::cerr << "[ERROR] Unable to open file '" << filepath << "'\n";
        return lines;
    }

    std::string line;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    return lines;
}



std::string clean_word(const std::string word) {
    std::string cleaned;

    for (char character : word) {
        if (!std::ispunct(character)) {
            cleaned += std::tolower(character);
        }
    }

    return cleaned;
}



std::vector<std::string> extract_words(std::string &line) {
    std::vector<std::string> words;
    std::stringstream ss(line);
    std::string buffer;

    while (ss >> buffer) {
        words.push_back(buffer);
    }

    return words;
}



template <typename T>
std::pair<T, int> find_entry_with_max_value(std::unordered_map<T, int> &um) {
    if (um.empty()) return std::make_pair(T(), 0);

    typename std::unordered_map<T, int>::iterator iter;
    std::pair<T, int> max_entry = *um.begin();

    for (const auto& [key, value] : um) {
        if (value > max_entry.second) {
            max_entry = std::make_pair(key, value);
        }
    }

    return max_entry;
}



TextFileStats analyze_text(const std::string &filepath) {
    std::vector<std::string> lines = read_lines(filepath);
    TextFileStats stats;
    stats.filepath = filepath;
    stats.lines_count = lines.size();
    std::unordered_map<std::string, int> words_frequency;
    std::unordered_map<char, int> chars_frequency;

    for (std::string &line : lines) {
        std::vector<std::string> words = extract_words(line);
        stats.words_count += words.size();

        for (std::string &word : words) {
            word = clean_word(word);
            stats.chars_count += word.length();
            words_frequency[word]++;

            for (char character : word) {
                chars_frequency[character]++;
            }
        }
    }

    stats.most_common_word = find_entry_with_max_value(words_frequency).first;
    stats.most_common_char = find_entry_with_max_value(chars_frequency).first;

    return stats;
}



void print_stats(const TextFileStats &stats) {
    std::cout << "{\n"
    << "  \"filepath\": \"" << stats.filepath << "\",\n"
    << "  \"chars_count\": " << stats.chars_count << ",\n"
    << "  \"words_count\": " << stats.words_count << ",\n"
    << "  \"lines_count\": " << stats.lines_count << ",\n"
    << "  \"most_common_char\": \"" << stats.most_common_char << "\",\n"
    << "  \"most_common_word\": \"" << stats.most_common_word << "\"\n"
    << "}" << std::endl;
}



int main() {
    std::string path;
    std::getline(std::cin, path);
    print_stats(analyze_text(path));
    return 0;
}
