#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <ctime>

// Function to generate a 6-digit OTP
std::string generate_otp() {
    std::string otp = "";
    for (int i = 0; i < 6; i++) {
        otp += std::to_string(rand() % 10);  // Generate a digit between 0 and 9
    }
    return otp;
}

// Function to save OTP to a file
void save_otp_to_file(const std::string &otp) {
    std::ofstream otp_file("otp.txt");
    if (otp_file.is_open()) {
        otp_file << otp;
        otp_file.close();
    } else {
        std::cerr << "Error opening file to save OTP\n";
    }
}

int main() {
    srand(time(0));  // Seed for random number generation

    // Generate OTP and save to file
    std::string otp = generate_otp();
    std::cout << otp << std::endl;  // Print the OTP (this is captured by Python)
    save_otp_to_file(otp);

    return 0;
}
