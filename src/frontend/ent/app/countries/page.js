"use client";
import {usePathname, useRouter, useSearchParams} from "next/navigation";
import {useCallback, useEffect, useState} from "react";
import {
    CircularProgress,
    Pagination,
    Paper,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow
} from "@mui/material";

export default function CountriesPage() {

    const searchParams = useSearchParams();
    const pathname = usePathname();
    const router = useRouter();
    const createQueryString = useCallback(
        (name, value) => {
            const params = new URLSearchParams(searchParams)
            params.set(name, value)

            return params.toString()
        },
        [searchParams]
    );
    const [data, setData] = useState(null);
    const [maxDataSize, setMaxDataSize] = useState(0);

    const page = parseInt(searchParams.get('page')) || 1;
    const PAGE_SIZE = 10;

    useEffect(() => {
    setData(null);

    // Fetch data from the server
    fetch(`http://localhost:20001/Countries/`)
      .then((response) => response.json())
      .then((responseData) => {
        console.log('Data fetched:', responseData);
        setData(responseData);  // Assuming your server response is an array
        // In this case, you may not have 'maxDataSize', but you can set it to the length of the array
        setMaxDataSize(responseData.length);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, [page]);

    return (
        <>
            <h1 sx={{fontSize: "100px"}}>Countries</h1>

            <TableContainer component={Paper}>
                <Table sx={{minWidth: 650}} aria-label="simple table">
                    <TableHead>
                        <TableRow sx={{backgroundColor: "lightgray"}}>
                            <TableCell component="th" width={"1px"} align="center">ID</TableCell>
                            <TableCell>Abreviation</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {data ?
                          data.map((row) => (
                            <TableRow key={row.id}>
                              <TableCell component="td" align="center">{row.id}</TableCell>
                              <TableCell component="td" scope="row">{row.name}</TableCell>
                            </TableRow>
                          )) :
                          <TableRow>
                            <TableCell colSpan={2}>
                              <CircularProgress/>
                            </TableCell>
                          </TableRow>
                        }
                    </TableBody>
                </Table>
            </TableContainer>
            {
                maxDataSize && <Pagination style={{color: "black", marginTop: 8}}
                                           variant="outlined" shape="rounded"
                                           color={"primary"}
                                           onChange={(e, v) => {
                                               router.push(pathname + '?' + createQueryString('page', v))
                                           }}
                                           page={page}
                                           count={Math.ceil(maxDataSize / PAGE_SIZE)}
                />
            }


        </>
    );
}