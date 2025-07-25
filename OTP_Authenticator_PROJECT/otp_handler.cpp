#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

void generateOTP() {
    srand(time(0)); // Seed for random number generation
    int otp = rand() % 900000 + 100000; // Generate a 6-digit OTP
    ofstream otpFile("otp.txt");
    if (otpFile.is_open()) {
        otpFile << otp;
        otpFile.close();
        cout << "OTP generated and saved in otp.txt\n";
    } else {
        cout << "Error: Unable to create otp.txt\n";
    }
}

void verifyOTP(const string& enteredOTP) {
    ifstream otpFile("otp.txt");
    string savedOTP;
    if (otpFile.is_open()) {
        getline(otpFile, savedOTP);
        otpFile.close();

        if (enteredOTP == savedOTP) {
            cout << "Verification successful!\n";
        } else {
            cout << "Incorrect OTP. Verification failed.\n";
        }
    } else {
        cout << "Error: Unable to read otp.txt\n";
    }
}

int main(int argc, char* argv[]) {
    if (argc == 2 && string(argv[1]) == "generate") {
        generateOTP();
    } else if (argc == 3 && string(argv[1]) == "verify") {
        verifyOTP(argv[2]);
    } else {
        cout << "Usage:\n";
        cout << "  otp_handler generate          - Generate OTP\n";
        cout << "  otp_handler verify <otp>      - Verify OTP\n";
    }
    return 0;
}
