#include <iostream>
#include <fstream>
#include <boost/tokenizer.hpp>

std::vector<std::vector<int> > find_all_paths(std::vector<std::vector<int> > h_map, int startr, int startc, int endr, int endc, std::vector<int> &path)
{
    path.push_back(h_map[startr][startc]);
    if ((startr == endr) && (startc == endc))
    {
        std::vector<std::vector<int> > ret;
        ret.push_back(path);
        return ret;
    }
}

int main()
{

    std::ifstream myfile("test_input.txt");
    std::vector<std::vector<int> > heightMap;
    if (myfile.is_open())
    {
        std::cout << "file is open" << std::endl;
        std::string line;
        while (getline(myfile, line))
        {
            std::vector<int> line_vector;
            for (auto it = line.begin(); it != line.end(); ++it)
            {
                //std::cout << (*it) << std::endl;
                line_vector.push_back((*it) - 48);
            }
            heightMap.push_back(line_vector);
        }

        myfile.close();
    }
    for (int r = 0; r < heightMap.size(); ++r)
    {
        std::cout << " r = " << r << std::endl;
        for (int c = 0; c < heightMap[r].size(); ++c)
        {
            std::cout << heightMap[r][c] << std::endl;
        }
    }

    return 0;
}
