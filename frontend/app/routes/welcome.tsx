import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { useNavigate } from "react-router";
import { useParams } from "react-router-dom";

export default function Welcome() {
  const { name } = useParams<{ name: string }>();
  const navigate = useNavigate();

  const handleLogout = () => {
    navigate("/");
  };

  return (
    <div className="bg-red-100 flex justify-center items-center min-h-screen">
      <Card className="mx-auto w-full max-w-sm text-center">
        <CardHeader>
          <CardTitle className="text-2xl font-bold">Welcome, {name}!</CardTitle>
        </CardHeader>
        <CardContent>
          <Button onClick={handleLogout} className="w-full">
            Log Out
          </Button>
        </CardContent>
      </Card>
    </div>
  );
}
